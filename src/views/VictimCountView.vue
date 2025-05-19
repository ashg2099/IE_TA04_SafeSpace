<template>
  <CrimeDashboard title="Australia Victim Counts" :dashboardUrl="victimCountUrl">
    <template #sidebar-content>
      <InforCard title="You Need To Be Aware">
        <p>Girls! Whenever possible, travel with friends or family as you're vulnerable to fall victim.</p>
      </InforCard>

      <AlertCard type="warning" icon="info-circle-fill">
        Female Victims are consistently higher than male victim counts across Australia
      </AlertCard>

      <AlertCard type="dark" icon="share-fill">
        Share safety information with your girls to <span class="fw-bold text-danger">promote street safety
          awareness</span>!
      </AlertCard>

    </template>
  </CrimeDashboard>
</template>

<script setup lang="ts">
import CrimeDashboard from '@/components/CrimeDashboard.vue';
import InforCard from '@/components/InforCard.vue'
import AlertCard from '@/components/AlertCard.vue';

const victimCountUrl = import.meta.env.VITE_TABLEAU_DASHBOARD_VICTIM_BY_GENDER;
</script>

<style scoped></style>
