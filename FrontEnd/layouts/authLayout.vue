<template>
    <div class="">
        <Header class="fixed z-50 bg-white" />
        <HomePage class="" />
    </div>

    <router-view />
</template>

<script>
import Header from '../components/header/Header.vue';
import HomePage from '../pages/HomePage.vue';
export default {
    components: { Header, HomePage }
}
</script>


<style>

</style>