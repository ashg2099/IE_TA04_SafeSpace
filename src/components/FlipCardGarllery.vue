<template>
  <div class="row g-3">
    <div v-for="card in cards" :key="card.frontText" class="col-sm-12 col-md-6 col-lg-3">
      <FlipCard :frontText="card.frontText" :backText="card.backText" :backgroundImage="card.bg" />
    </div>
  </div>


</template>

<script setup lang="ts">
import FlipCard from '@/components/FlipCard.vue'
import blue from '@/assets/blue.svg'
import green from '@/assets/green.svg'
import red from '@/assets/red.svg'
import yellow from '@/assets/yellow.svg'

interface Card {
  frontText: string
  backText: string
  bg: string
}

const cards: Card[] = [
  {
    frontText: 'Thoughtful,Introspective,Focused',
    backText: 'You might enjoy Brazilian Jiu-Jitsu. It’s a thoughtful and technical martial art where strategy matters more than strength. Ideal for those who prefer focus, patience, and subtle precision.',
    bg: blue,
  },
  {
    frontText: 'Bold,Energetic,Fearless',
    backText: 'You could try Muay Thai. It’s a dynamic and expressive martial art that matches your energy. Made for those who thrive in action and intensity.',
    bg: yellow,
  },
  {
    frontText: 'Ambient,Balanced,Adaptable',
    backText: 'Perhaps you’ll enjoy Kickboxing, it’s a versatile style that blends structure with spontaneity. It offers room for focused self-improvement and high-energy release.',
    bg: red,
  },
  {
    frontText: 'Curious,Observant,Analytical',
    backText: 'You could try Judo — a martial art where precision and problem-solving shine. Every grip and throw is a mental puzzle, perfect for minds that love to think in motion.',
    bg: green,
  }
]
</script>
