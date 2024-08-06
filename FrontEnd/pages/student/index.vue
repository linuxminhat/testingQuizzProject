<template>
    <student-sidebar />
    <router-view />
</template>

<script>
import StudentSidebar from '../../components/sidebar/StudentSidebar.vue'
export default {
    components: { StudentSidebar },

}
</script>

<style>

</style>