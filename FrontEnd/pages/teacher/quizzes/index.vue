<template>

    <h1 class="text-2xl ml-10 mt-5">Bộ sưu tập</h1>
    <div class="flex justify-end m-4 -mt-4 mr-8">
        <addform />
    </div>
    <div class="flex flex-wrap">

        <Collection v-for="(item, index) in collections" :key="index" :collection="item" @click="getName(item.name)" />

    </div>

    <router-view />
</template>

<script>
import { defineComponent, ref, onMounted, watch } from 'vue';
import Collection from '../../../components/collection/Collection.vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';
import Addform from '../../../components/modal/Addform.vue';
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";

export default defineComponent({
    components: {
        Collection,
        Addform,
        DownOutlined,
        RightOutlined,

    },
    setup() {
        const collections = ref([]);
        const teacherStore = useTeacherStore();




        const getName = (name) => {
            teacherStore.collectionName = name;
        };
        onMounted(async () => {
            collections.value = await teacherStore.getCollections();
        });


        watch(() => teacherStore.collections, (newCollections) => {
            collections.value = newCollections;
        });

        return {
            collections,


            getName
        };
    }
});
</script>

<style>

</style>