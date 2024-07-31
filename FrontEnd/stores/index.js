import { Pinia } from "pinia";
import { createPinia, setActivePinia } from "../src/index.js";

import useAuthStore from "./modules/auth.js";

const pinia = createPinia();
setActivePinia(pinia);
pinia.use(useAuthStore);

export default pinia;
