export function authMiddleware(to, from, next) {
  if (localStorage.getItem("role") === "student") {
    next();
  } else {
    next("/login");
  }
}
