<template>
  <div class="col-md-6 my-4">
    <div class="card border-0 h-100">
      <div class="card-body text-center d-flex flex-column">

        <div class="mb-4">
          <img :src="imageUrl" :alt="title" class="img-fluid rounded">
        </div>

        <div class="flex-grow-1">
          <slot></slot>
        </div>

        <div class="mt-4">
          <button class="btn btn-light btn-lg px-4" @click="navigateToPage">{{ buttonText }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
interface CardProps {
  imageUrl: string;
  title: string;
  buttonText: string;
  routePath: string;
}
const props = defineProps<CardProps>();
const router = useRouter();

const navigateToPage = () => {
  router.push(props.routePath);
};
</script>
