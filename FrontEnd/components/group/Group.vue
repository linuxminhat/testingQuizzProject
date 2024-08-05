<template>
    <div class="flex flex-wrap">
        <div v-for="card in cards" :key="card.id"
            class="m-4 w-60 h-72 bg-slate-100 rounded-3xl text-gray-500 p-4 flex flex-col items-start justify-center gap-3 hover:bg-gray-400 hover:shadow-2xl hover:shadow-sky-400 hover:text-white hover:cursor-pointer transition-shadow">
            <edit-group class="fixed text-end items-end hover:text-white" :group="card" />
            <div class="w-52 h-40 bg-slate-300 rounded-2xl" @click="getGroupId(card.id,card.name)">
                <img :src=" imgUrl +'static/'+ card.image_path"
                    class=" relative h-full w-full items-center justify-center rounded-md" alt="">
            </div>
            <div class="">
                <p class="font-extrabold">{{ card.name }}</p>
                <p class="">{{ card.description }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, toRefs } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
import { useRouter, useRoute } from 'vue-router';
import EditGroup from '../modal/EditGroup.vue';

export default {

    props: {
        cards: {
            type: Array,
            required: true
        }
    },
    components: { EditGroup },
    setup(props) {
        const { cards } = toRefs(props);
        const router = useRouter();
        const route = useRoute();
        const imgUrl = import.meta.env.VITE_APP_API;
        console.log(imgUrl)
        const getGroupId = (id, name) => {
            const teacherStore = useTeacherStore();
            teacherStore.groupId = id;
            teacherStore.groupName = name;

            if (route.path == '/teacher/group') {
                router.push({ name: 'teacher-group-detail', params: { id: id } });
            } else {
                router.push({ name: 'student-group-detail', params: { id: id } });
            }
        };

        return {
            cards,

            imgUrl,
            getGroupId
        };
    }
}
</script>

<style>

</style>