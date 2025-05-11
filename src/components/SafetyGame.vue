<template>
  <div
    class="game-container"
    :class="{ fullscreen: isMaximized }"
  >
    <!-- Title Bar -->
    <div class="title-bar">
      <div class="window-buttons">
        <span class="button close" @click="closeWindow"></span>
        <span class="button maximize" @click="maximizeWindow"></span>
        <span class="button minimize" @click="minimizeWindow"></span>
      </div>
      <h2 class="game-title">Safety Game</h2>
    </div>

    <!-- Chat Window -->
    <div class="chat-window">
      <div class="chat-box">
        <div
          v-for="(message, index) in messages"
          :key="index"
          class="message"
        >
          <p v-html="message.text"></p>
        </div>
      </div>
    </div>

    <!-- Input Box -->
    <div class="input-box">
      <div v-if="currentStep === 1" class="button-container">
        <button
          class="answer-button"
          @click="answerQuestion('street-harassment')"
        >
          Street Harassment
        </button>
        <button
          class="answer-button"
          @click="answerQuestion('public-transport')"
        >
          Public Transport Harassment
        </button>
        <button
          class="answer-button"
          @click="answerQuestion('workplace')"
        >
          Workplace Harassment
        </button>
      </div>
      <div v-if="currentStep > 1 && currentStep < 4">
        <button @click="nextStep">Next</button>
      </div>
      <div v-if="currentStep === 4">
        <button @click="resetGame">Re-select</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isMaximized = ref(false)

function maximizeWindow() {
  isMaximized.value = true
}

function minimizeWindow() {
  isMaximized.value = false
}

function closeWindow() {
  router.push({ name: 'home' })
}

// Game logic
const currentStep = ref(1)
const messages = ref([{ text: 'Are you ready? Start the game!!!' }])

const safetyTips = {
  'street-harassment': [
    '1. Walk in well-lit areas and avoid isolated streets.',
    '2. Be assertive and let the person know their behavior is inappropriate.',
    '3. Stay calm and try to find a safe place or group of people.',
    '4. Use your phone to alert someone if you feel unsafe.',
  ],
  'public-transport': [
    '1. Sit near the driver or conductor if possible.',
    '2. Stay alert and avoid distractions, like your phone.',
    '3. Don’t be afraid to make noise or draw attention if you feel threatened.',
    '4. If you feel unsafe, get off at the next stop and find a safe place.',
  ],
  'workplace': [
    '1. Speak up about inappropriate behavior to HR or your supervisor.',
    '2. Document incidents of harassment or inappropriate behavior.',
    '3. Seek support from colleagues or trusted individuals.',
    '4. Know your rights in the workplace regarding harassment.',
  ],
}

let selectedScenario = ''

function answerQuestion(option) {
  selectedScenario = option
  messages.value.push({
    text: `You choice is <strong>${option.replace('-', ' ')}</strong>`,
  })
  currentStep.value = 2
}

function nextStep() {
  if (currentStep.value === 2) {
    messages.value.push({
      text: "Let's see what you should do in this situation.",
    })
    currentStep.value = 3
  } else if (currentStep.value === 3) {
    const tips = safetyTips[selectedScenario].join('<br><br>')
    messages.value.push({
      text: `<strong>Here are some safety tips:</strong><br><br>${tips}`,
    })
    currentStep.value = 4
  }
}

function resetGame() {
  currentStep.value = 1
  messages.value = [{ text: 'Are you ready? Start the game!!!' }]
}
</script>

<style scoped>
/* Fullscreen override */
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
/* Make children fill width & remove corner radius in fullscreen */
.game-container.fullscreen .title-bar,
.game-container.fullscreen .chat-window,
.game-container.fullscreen .input-box {
  width: 100% !important;
  max-width: none !important;
  border-radius: 0 !important;
}
/* Stretch chat-window to fill available height */
.game-container.fullscreen .chat-window {
  flex: 1;
  min-height: 0;
}

/* Default layout */
.game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

/* Title Bar */
.title-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 90%;
  max-width: 800px;
  padding: 15px;
  background-color: #8E44AD;
  border-radius: 8px 8px 0 0;
  color: white;
}
.window-buttons {
  display: flex;
  gap: 10px;
}
.window-buttons .button {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background-color: white;
  cursor: pointer;
}
.window-buttons .close   { background-color: #FF4C4C; }
.window-buttons .maximize{ background-color: #FFBD4A; }
.window-buttons .minimize{ background-color: #4CAF50; }
.game-title {
  font-size: 24px;
  font-weight: bold;
  flex-grow: 1;
  text-align: center;
}

/* Chat Window */
.chat-window {
  width: 90%;
  max-width: 800px;
  background: url('@/assets/background.jpg') no-repeat center center;
  background-size: cover;
  border: 2px solid #ffffff;
  border-radius: 8px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  min-height: 400px;
}
.chat-box {
  flex-grow: 1;
  overflow-y: auto;
}
.message {
  display: block;            
  width: fit-content;        
  max-width: 70%;            
  margin: 10px 0 10px auto; 
  padding: 10px;
  background-color: #4169E1;
  color: white;
  border-radius: 15px;
  text-align: center;
  font-weight: bold;
  word-wrap: break-word;
}

/* Input Box */
.input-box {
  display: flex;
  justify-content: center;
  padding: 15px;
  background-color: #8E44AD;
  border-radius: 0 0 8px 8px;
  width: 90%;
  max-width: 800px;
}
.button-container {
  display: flex;
  justify-content: center;
  gap: 15px;
  width: 100%;
}

/* Buttons */
.answer-button,
button {
  flex: 1;
  padding: 15px;
  background-color: #198bc4;
  color: white;
  border: none;
  border-radius: 25px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
}
.answer-button:hover,
button:hover {
  background-color: #2980b9;
}
button:disabled {
  background-color: #ddd;
  cursor: not-allowed;
}
</style>
