import Vue from 'vue'
import store from '@/store'
import router from '@/router'


import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


 import VueAnalytics from 'vue-analytics'


import * as Sentry from "@sentry/vue"
import { Integrations } from "@sentry/tracing";


import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false


// Sentry for logging frontend errors
Sentry.init({
  Vue: Vue,
  dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN,
  integrations: [new Integrations.BrowserTracing()],
  tracingOptions: {
    trackComponents: true,
  },
  logError: process.env.NODE_ENV === 'development'
});



// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {
  id: process.env.VUE_APP_GOOGLE_ANALYTICS,
  router
})




new Vue({
  router,
  store,
  
render: h => h(App)
}).$mount('#app')
