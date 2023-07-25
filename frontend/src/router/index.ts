import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import MovieView from '../views/MovieView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
