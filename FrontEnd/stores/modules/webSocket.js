import { defineStore } from "pinia";

export const useWebSocketStore = defineStore({
  id: "webSocket",
  state: () => ({
    WS: null,
  }),
  actions: {
    connect() {
      this.WS = new WebSocket(`ws://localhost:4444/student`);
      this.WS.onopen = (event) => {
        console.log("Connection opened", event);

        let token = localStorage.getItem("token");

        let auth = {
          command: "AUTHENTICATE",
          detail: {
            token: token,
          },
        };
        this.WS.send(JSON.stringify(auth));
        localStorage.setItem("authTest", auth);
      };

      this.WS.onmessage = (event) => {
        console.log("Message received from server:", event.data);
      };
    },
  },
});
