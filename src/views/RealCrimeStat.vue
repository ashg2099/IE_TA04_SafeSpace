<template>
  <InforCard card-class="shadow-sm rounded bg-light border-0 mb-4">
    <OffenseCountView />
  </InforCard>

  <InforCard card-class="card shadow-sm rounded bg-light border-0 mb-4">
    <VictimCountView />
  </InforCard>
</template>

<script setup lang="ts">
import OffenseCountView from '@/views/OffenseCountView.vue';
import VictimCountView from '@/views/VictimCountView.vue';
import InforCard from '@/components/InforCard.vue';
</script>


<style></style>
