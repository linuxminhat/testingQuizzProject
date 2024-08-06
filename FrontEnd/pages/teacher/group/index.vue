<template>
    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleGroup1">
        <DownOutlined v-if="showGroup1" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4 ">Nhóm</h1>

        <add-group-vue class="absolute right-16 mt-8" />

    </div>

    <div v-show="showGroup1" class="scroll-container">
        <Group :cards="groupShows" />
    </div>

    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleGroup2">
        <DownOutlined v-if="showGroup2" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4 ">Nhóm đã ẩn</h1>
    </div>
    <div v-show="showGroup2" class="scroll-container">
        <Group :cards="groupHiddens" />
    </div>


</template>

<script>
import { onMounted, ref } from 'vue';
import Group from '../../../components/group/Group.vue'
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";
import AddGroupVue from '../../../components/modal/AddGroup.vue';
import { useTeacherStore } from '../../../stores/modules/teacher';

export default {
    components: { Group, DownOutlined, RightOutlined, AddGroupVue },
    setup() {
        const showGroup1 = ref(true);
        const showGroup2 = ref(false);
        const groupShows = ref([]);
        const groupHiddens = ref([]);

        const teacherStore = useTeacherStore();
        onMounted(async () => {

            groupShows.value = await teacherStore.getGroups();
            groupHiddens.value = await teacherStore.getHiddenGroups();
            console.log(groupShows.value)
        })

        const toggleGroup1 = () => {
            showGroup1.value = !showGroup1.value;
        };

        const toggleGroup2 = () => {
            showGroup2.value = !showGroup2.value;

        };

        return { showGroup1, showGroup2, groupShows, groupHiddens, toggleGroup1, toggleGroup2 };
    }
}
</script>

<style>
.scroll-container {
    max-height: 80vh; 
    overflow-y: auto;
}
</style>