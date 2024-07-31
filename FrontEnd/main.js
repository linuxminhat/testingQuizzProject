import { createApp } from "vue";
import { createPinia } from "pinia";
import "./style.css";
import "./assets/style.css";
import router from "./router/index.js";
import App from "./App.vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";

library.add(fas, fab, far);
import Toast from "vue-toastification";
// Import the CSS or use your own!
import "vue-toastification/dist/index.css";
import "ant-design-vue/dist/reset.css";
import {
  Calendar,
  Menu,
  Layout,
  Avatar,
  Badge,
  Modal,
  Button,
  Input,
  Table,
  Spin,
} from "ant-design-vue";

const app = createApp(App);
app.use(router);
app.use(Layout);
app.use(Avatar);
app.use(Badge);
app.use(Modal);
app.use(Button);
app.use(Input);
app.use(Calendar);
app.use(Menu);
app.use(Table);
app.use(Spin);
app.use(Toast);

app.use(createPinia());
app.component("fa", FontAwesomeIcon);
app.mount("#app");
