<template>
  <div class="game-container" :class="{ fullscreen: isMaximized }">
    <!-- Title Bar -->
    <div class="title-bar">
      <div class="window-buttons">
        <span class="window-button close" @click="closeWindow">
          <i class="fas fa-times"></i>
        </span>
        <span class="window-button maximize" @click="maximizeWindow">
          <i class="fas fa-square"></i>
        </span>
        <span class="window-button minimize" @click="minimizeWindow">
          <i class="fas fa-minus"></i>
        </span>
      </div>
      <h2 class="game-title">Safety Game</h2>
    </div>

    <!-- Chat Window -->
    <div class="chat-window">
      <div class="chat-box" ref="chatBoxRef">
        <div v-for="(message, index) in messages" :key="index" class="message">
          <p v-html="message.text"></p>
        </div>
      </div>
    </div>

    <!-- Input Box -->
    <div class="input-box">
      <!-- Step 1: Scenario Selection -->
      <div v-if="currentStep === 1" class="button-container">
        <button class="answer-button" @click="startScenario('street-harassment')">
          Walking Alone at Night
        </button>
        <button class="answer-button" @click="startScenario('public-transport')">
          Harassment on Public Transport
        </button>
        <button class="answer-button" @click="startScenario('workplace')">
          Workplace Harassment
        </button>
        <button class="answer-button" @click="startScenario('online-harassment')">
          Online Harassment
        </button>
        <button class="answer-button" @click="startScenario('park-safety')">Park Safety</button>
      </div>

      <!-- Step 2: Quiz Question Options -->
      <div v-if="currentStep === 2" class="button-container">
        <button
          class="answer-button"
          v-for="opt in currentQuiz.questions[questionIndex].options"
          :key="opt.value"
          @click="selectAnswer(opt.value)"
        >
          {{ opt.label }}
        </button>
      </div>

      <!-- Step 3: Restart -->
      <div v-if="currentStep === 3" class="button-container">
        <button @click="resetGame">Re-select Scenario</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isMaximized = ref(false)
const chatBoxRef = ref(null)

function maximizeWindow() {
  isMaximized.value = true
}

function minimizeWindow() {
  isMaximized.value = false
}

function closeWindow() {
  router.push({ name: 'home' })
}

// Quiz data: multiple questions per scenario
const quizzes = {
  'street-harassment': {
    questions: [
      {
        question: 'Walking alone at night, you notice someone following you. What do you do first?',
        options: [
          { value: 'ignore', label: 'Ignore and keep walking' },
          { value: 'call', label: 'Call for help immediately' },
          { value: 'confront', label: 'Confront the person' },
        ],
        feedback: {
          ignore: 'Ignoring may embolden them and increase risk.',
          call: 'Correct! Calling for help can alert others and deter them.',
          confront: 'Confrontation can be risky; it’s safer to call for help.',
        },
      },
      {
        question: 'What is a safe place you should head towards?',
        options: [
          { value: 'dark', label: 'Darker side street' },
          { value: 'lit', label: 'Well-lit area with people' },
          { value: 'home', label: 'Go home alone' },
        ],
        feedback: {
          dark: 'Dark areas are unsafe; avoid them.',
          lit: 'Correct! Staying in well-lit crowded areas is safer.',
          home: 'Going home may leave you isolated; find a safe public spot.',
        },
      },
    ],
    tips: [
      'Move to a well-lit, populated area.',
      'Call emergency services or a friend.',
      'Stay aware and keep your phone ready.',
    ],
  },
  'public-transport': {
    questions: [
      {
        question: 'On public transport, someone harasses you. What is your first action?',
        options: [
          { value: 'move', label: 'Move seats' },
          { value: 'alert', label: 'Alert the driver/authority' },
          { value: 'speak', label: 'Confront them directly' },
        ],
        feedback: {
          move: 'Moving is passive and may not stop them.',
          alert: 'Correct! Alerting authority ensures help arrives.',
          speak: 'Direct confrontation can escalate the situation.',
        },
      },
      {
        question: 'Which seat location is safest?',
        options: [
          { value: 'rear', label: 'Back of the vehicle' },
          { value: 'front', label: 'Near the driver' },
          { value: 'middle', label: 'Middle section' },
        ],
        feedback: {
          rear: 'Rear seats are away from help; avoid them.',
          front: 'Correct! Near the driver you have access to assistance.',
          middle: 'Middle can be safer but driver proximity is best.',
        },
      },
    ],
    tips: [
      'Sit near the driver or exit doors.',
      'Use emergency alarms or inform staff.',
      'Keep phone out to call for help if needed.',
    ],
  },
  workplace: {
    questions: [
      {
        question: 'A colleague makes unwelcome comments. What is your first step?',
        options: [
          { value: 'ignore', label: 'Ignore and stay quiet' },
          { value: 'document', label: 'Document the incident' },
          { value: 'public', label: 'Confront publicly' },
        ],
        feedback: {
          ignore: 'Ignoring allows harassment to continue.',
          document: 'Correct! Documenting helps build a report.',
          public: 'Public confrontation can escalate conflict.',
        },
      },
      {
        question: 'Who should you report to?',
        options: [
          { value: 'friend', label: 'A coworker friend' },
          { value: 'hr', label: 'Human Resources' },
          { value: 'social', label: 'Company social group' },
        ],
        feedback: {
          friend: 'Friends can support but not resolve officially.',
          hr: 'Correct! HR handles formal complaints.',
          social: 'Social groups are informal; use official channels.',
        },
      },
    ],
    tips: [
      'Keep records of all incidents.',
      'Report formally to HR.',
      'Seek support from management or legal.',
    ],
  },
  'online-harassment': {
    questions: [
      {
        question: 'You receive harassing messages online. What do you do first?',
        options: [
          { value: 'block', label: 'Block the user' },
          { value: 'report', label: 'Report to the platform' },
          { value: 'reply', label: 'Reply and defend yourself' },
        ],
        feedback: {
          block: 'Blocking stops direct harassment and is good first step.',
          report: 'Correct! Reporting helps enforce community standards.',
          reply: 'Replying can escalate the situation.',
        },
      },
      {
        question: 'What evidence should you keep?',
        options: [
          { value: 'screenshots', label: 'Take screenshots' },
          { value: 'memory', label: 'Rely on memory' },
          { value: 'none', label: 'No evidence needed' },
        ],
        feedback: {
          screenshots: 'Correct! Screenshots provide verifiable proof.',
          memory: 'Memory alone is not sufficient evidence.',
          none: 'It’s important to keep records of harassment.',
        },
      },
    ],
    tips: [
      'Block and mute harassers immediately.',
      'Report content to moderators.',
      'Save evidence like screenshots.',
    ],
  },
  'park-safety': {
    questions: [
      {
        question: 'In a secluded park at night, you feel unsafe. What’s your first move?',
        options: [
          { value: 'stay', label: 'Stay and wait' },
          { value: 'leave', label: 'Leave immediately' },
          { value: 'call', label: 'Call friend or authorities' },
        ],
        feedback: {
          stay: 'Staying increases risk; better to leave.',
          leave: 'Correct! Exiting reduces potential danger.',
          call: 'Calling helps, but prioritize leaving the area.',
        },
      },
      {
        question: 'Where should you head?',
        options: [
          { value: 'road', label: 'Nearby road or busy area' },
          { value: 'home', label: 'Your home alone' },
          { value: 'bench', label: 'Park bench to wait' },
        ],
        feedback: {
          road: 'Correct! Seek a well-lit, populated area.',
          home: 'Home may not be safe; choose public spot.',
          bench: 'Waiting in park is unsafe.',
        },
      },
    ],
    tips: [
      'Leave the park immediately.',
      'Call someone you trust or security services.',
      'Stay in well-lit areas.',
    ],
  },
}

const currentStep = ref(1)
const messages = ref([{ text: 'Are you ready? START GAME!!!' }])
const currentQuiz = reactive({ questions: [], tips: [] })
const questionIndex = ref(0)

// Auto-scroll chat on new messages
watch(
  messages,
  async () => {
    await nextTick()
    const box = chatBoxRef.value
    if (box) box.scrollTop = box.scrollHeight
  },
  { deep: true, flush: 'post' }
)

function startScenario(key) {
  messages.value.push({ text: `Scenario: <strong>${key.replace(/-/g, ' ')}</strong>` })
  const quizData = quizzes[key]
  currentQuiz.questions = quizData.questions
  currentQuiz.tips = quizData.tips
  questionIndex.value = 0
  messages.value.push({ text: currentQuiz.questions[0].question })
  currentStep.value = 2
}

function selectAnswer(choice) {
  const q = currentQuiz.questions[questionIndex.value]
  const label = q.options.find((o) => o.value === choice).label
  messages.value.push({ text: `Your answer: <strong>${label}</strong>` })
  messages.value.push({ text: q.feedback[choice] })
  if (questionIndex.value < currentQuiz.questions.length - 1) {
    questionIndex.value++
    messages.value.push({ text: currentQuiz.questions[questionIndex.value].question })
  } else {
    const html = currentQuiz.tips.map((t) => `<li>${t}</li>`).join('')
    messages.value.push({ text: `<strong>Safety Tips:</strong><ul>${html}</ul>` })
    currentStep.value = 3
  }
}

function resetGame() {
  currentStep.value = 1
  messages.value = [{ text: 'Ready for another scenario? 🚀' }]
}
</script>

<style scoped>
.window-buttons {
  display: flex;
  gap: 8px;
}

.window-buttons .window-button {
  width: 18px;
  height: 18px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background-color: #fff;
  cursor: pointer;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

.window-buttons .close {
  background-color: #ff4c4c;
}

.window-buttons .maximize {
  background-color: #ffbd4a;
}

.window-buttons .minimize {
  background-color: #4caf50;
}

.window-buttons .window-button i {
  font-size: 12px;
  color: #333;
}

.game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.game-container.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  margin: 0;
  padding: 0;
  z-index: 9999;
  background: white;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.game-container.fullscreen .title-bar,
.game-container.fullscreen .chat-window,
.game-container.fullscreen .input-box {
  width: 100% !important;
  max-width: none !important;
  border-radius: 0 !important;
}

.game-container.fullscreen .chat-window {
  flex: 1;
  min-height: 0;
}

.title-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 90%;
  max-width: 800px;
  padding: 15px;
  background: linear-gradient(135deg, #8e44ad, #6c3483);
  border-radius: 8px 8px 0 0;
  color: #fff;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.game-title {
  flex: 1;
  text-align: center;
  font-size: 20px;
  font-weight: 700;
}

.chat-window {
  width: 90%;
  max-width: 800px;
  background: url('@/assets/background.jpg') no-repeat center/cover;
  border: 2px solid #fff;
  border-radius: 0 0 8px 8px;
  display: flex;
  flex-direction: column;
  padding: 20px 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  height: 500px;
  overflow-y: auto;
}

.chat-box {
  flex: 1;
  overflow-y: auto;
}

.message {
  display: block;
  width: fit-content;
  max-width: 70%;
  margin: 12px 0 12px auto;
  padding: 12px 16px;
  background: #3498db;
  color: #fff;
  border-radius: 12px;
  font-weight: 600;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
  text-align: left;
  word-wrap: break-word;
}

.message ul {
  margin: 8px 0 0;
  padding-left: 20px;
}

.message li {
  margin-bottom: 6px;
}

.input-box {
  width: 90%;
  max-width: 800px;
  display: flex;
  justify-content: center;
  padding: 15px;
  background: linear-gradient(135deg, #6c3483, #8e44ad);
  border-radius: 0 0 8px 8px;
}

.button-container {
  display: flex;
  gap: 12px;
  width: 100%;
}

.answer-button,
button {
  flex: 1;
  padding: 12px;
  background: #1abc9c;
  color: #fff;
  border: none;
  border-radius: 20px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
  transition: background 0.2s;
}

.answer-button:hover,
button:hover {
  background: #16a085;
}

button:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
}
</style>
