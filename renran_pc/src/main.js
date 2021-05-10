// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import settings from "./settings";
// 导入 饿了么Ui
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import "../static/CSS/reset.css";

// 导入 axios
import axios from "axios";

Vue.use(ElementUI); // 调用插件

// 允许ajax发送请求时附带cookie，设置为不允许
axios.defaults.withCredentials =false
Vue.prototype.$axios = axios

// 增设配置文件
Vue.prototype.$settings = settings

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  model:history,
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
