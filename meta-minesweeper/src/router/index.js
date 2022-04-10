import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import VideoDetail from '../components/VideoDetail.vue'
import NotFoundView from '../views/NotFoundView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  // {
  //   path: '/player/:id(\\d+)',
  //   name: 'player',
  //   component: Player
  // },
  {
    path: '/video_/:file',
    name: 'video_',
    component: VideoDetail,
    props($route) {
      return {
        file: $route.params.file,
      }
    }
  },
  // {
  //   path: '/:notfound(.*)',
  //   name: '404',
  //   component: NotFoundView
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
