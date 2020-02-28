import Vue from "vue";
import VueRouter from "vue-router";
import Index from "../views/Index.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "index",
    component: Index
  } //去除#号
];

const router = new VueRouter({
  routes,
  mode: "history" //去除#号
});

export default router;
