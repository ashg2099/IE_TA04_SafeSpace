<template>
  <main>
    <section class="d-flex justify-content-between align-items-center px-3 pb-3">
      <p class="fs-5 flex-grow-1 m-0 text-center">
        With 1 in 5 women experiencing stalking since the age of 15,<br />
        learning self-defense isn’t just a choice — it’s a powerful step toward safety and confidence.
      </p>
      <div class="ms-3">
        <ScrollDown text="Flip Cards to Find a Suitable Defense Style" iconClass="bi bi-back"
          buttonClass="btn btn-warning" targetId='flip-card' />
      </div>
    </section>
    <SelfDefenseClass />
    <section class="text-center pb-3 pt-5 px-3">
      <h2 class="fw-bold mb-3">
        Not sure which self-defense style suits you?
      </h2>

      <p class="fs-5" id="flip-card">
        Take this quick, fun flip cards to find your perfect match — based on your<br />
        personality, not your punches!
      </p>
    </section>
    <FlipCardGarllery />
  </main>
</template>

<script setup lang="ts">
import ScrollDown from '@/components/ScrollDown.vue';
import FlipCardGarllery from '@/components/FlipCardGarllery.vue';
import SelfDefenseClass from '@/components/SelfDefenseClass.vue';
</script>
