import { createRouter, createWebHistory } from 'vue-router'
import FirstView from '../views/FirstView.vue'

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
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ExploreCrimeStat.vue'),
    },
    {
      path: '/check-nearby-community',
      name: 'check-nearby-community',
      component: () => import('../views/CheckNearbyCommunityView.vue'),
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
