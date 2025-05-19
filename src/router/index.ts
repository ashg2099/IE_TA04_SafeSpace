import { createRouter, createWebHistory } from 'vue-router'

// Import existing views
import FirstView from '@/views/FirstView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: FirstView,
    },
    {
      path: '/explore-crime-stat',
      name: 'explore-crime-stat',
      component: () => import('@/views/ExploreCrimeStat.vue'),
    },
    {
      path: '/check-nearby-community',
      name: 'check-nearby-community',
      component: () => import('@/views/CheckNearbyCommunityView.vue'),
    },

    // New routes for the Gamified Safety Tips Epic
    {
      path: '/safety-game',
      name: 'safety-game',
      component: () => import('@/components/SafetyGame.vue'),
    },
    {
      path: '/self-defense',
      name: 'self-defense',
      component: () => import('@/views/SelfDefenseView.vue'),
    },
  ],

  scrollBehavior(to, from, savedPosition) {
    return new Promise((resolve) => {
      if (savedPosition) {
        resolve(savedPosition)
      } else {
        resolve({ left: 0, top: 0 })
      }
    })
  },
})

export default router
