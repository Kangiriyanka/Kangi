import { createMemoryHistory, createRouter } from 'vue-router'

import HomeView from './pages/HomeView.vue'
import GraphView from './pages/GraphView.vue'
import WritingView from './pages/WritingView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/graphs', component: GraphView },
  { path: '/writing', component: WritingView },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router