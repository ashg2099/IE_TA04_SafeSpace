<template>
  <main>
    <div class="p-4 p-md-5 mb-4 rounded text-body-emphasis bg-light">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <h1 class="display-5 fw-bold">Have you ever felt unsafe in the cities?</h1>
          <p class="lead my-3 fs-3">
            Hey, it's more than normal than you think<br>
            - Actually, only 50% of Australian women feel safe walking alone at night, according to the OECD Better Life
            Index
          </p>
          <ScrollDown targetId="additional-content" text="Discover more statistics" buttonClass="btn-dark"
            iconClass="bi bi-arrow-bar-down" additionalClass="mt-5" />
        </div>
        <div class="col-lg-6 text-end">
          <img src="@/assets/sad.svg" class="img-fluid rounded" alt="Welcome image1">
        </div>
      </div>
    </div>

    <div class="p-4 p-md-5 mb-4 rounded text-body-emphasis bg-warning text-end">
      <div class="row align-items-center">
        <!-- change-to-real-picture -->
        <div class="col-lg-6 text-start">
          <!-- <svg aria-label="Welcome image" width="100%" height="800" preserveAspectRatio="xMidYMid slice"
            focusable="false"> -->
          <img src="@/assets/group-happy.svg" class="img-fluid rounded" alt="Welcome image2" />
          <!-- </svg> -->
        </div>
        <div class="col-lg-6">
          <h1 class="display-5 fw-bold">Welcome to the SafeSpace</h1>
          <p class="lead my-3 fs-3">
            We're here to help you navigate Melbourne CBD with confidence, not fear. Here you can explore crime
            statistics, practical safety tips, and expert advice to stay prepared in any situation.
          </p>
        </div>
      </div>
    </div>

    <div class="p-3 mb-4">
      <h1 class="mb-4 display-5 fw-bold">What we can do for you?</h1>

      <div class="row bg-light" id="additional-content">
        <HomeFeatureCard v-for="card in featureCards" :key="card.id" :image-url="card.imageUrl" :title="card.title"
          :button-text="card.buttonText" :route-path="card.routePath">
          <h3> {{ card.title }}</h3>
        </HomeFeatureCard>
      </div>
    </div>
  </main>

</template>

<script setup lang="ts">
import { ref } from 'vue'
import HomeFeatureCard from '@/components/HomeFeatureCard.vue'
import datavis from '@/assets/data-vis.svg'
import game from '@/assets/game.svg'
import pedlight from '@/assets/pedlight.svg'
import ScrollDown from '../components/ScrollDown.vue';
import selfdefense from '@/assets/self-defense.svg';

interface FeatureCardType {
  id: number;
  imageUrl: string;
  title: string;
  buttonText: string;
  routePath: string;
}


const featureCards = ref<FeatureCardType[]>([
  {
    id: 1,
    imageUrl: datavis,
    title: 'Want to know what happened in Melbourne last few years?',
    buttonText: 'Explore Crime statistics',
    routePath: '/explore-crime-stat'
  },
  {
    id: 2,
    imageUrl: pedlight,
    title: "Curious which areas around you are buzzing and well-lit? Let's find out!",
    buttonText: 'Check Nearby Community',
    routePath: '/check-nearby-community'
  },
  {
    id: 3,
    imageUrl: game,
    title: 'Want to know if you can survive under different scenarios. Learn best practices through play.',
    buttonText: 'Try the safety challenge',
    routePath: '/check-nearby-community'
  },
  {
    id: 4,
    imageUrl: selfdefense,
    title: "Want to feel safer and more confident in your surroundings? Discover self-denfese classes tailored to your personality",
    buttonText: 'Find a self-defense class',
    routePath: '/check-nearby-community' //need to change later
  }
])

</script>

<style></style>
