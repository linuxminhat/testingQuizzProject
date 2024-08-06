<template>
    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleGroup1">
        <DownOutlined v-if="showGroup1" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4">Nhóm</h1>

    </div>
    <join-group class="fixed -mt-10 mr-10 flex justify-end text-end right-0" />
    <div v-show="showGroup1" class="scroll-container">
        <Group :cards="cardshow" />
    </div>

    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleGroup2">
        <DownOutlined v-if="showGroup2" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4">Nhóm đã ẩn</h1>
    </div>
    <div v-show="showGroup2" class="scroll-container">
        <Group :cards="cardshidden" />
    </div>

    <router-view />
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import Group from '../../../components/group/Group.vue'
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";
import { useStudentStore } from '../../../stores/modules/student.js';
import JoinGroup from '../../../components/modal/JoinGroup.vue';
export default defineComponent({
    components: { Group, DownOutlined, RightOutlined, JoinGroup },
    setup() {
        const showGroup1 = ref(true);
        const showGroup2 = ref(false);
        const cardshow = ref([]);
        const cardshidden = ref([]);

        const toggleGroup1 = () => {
            showGroup1.value = !showGroup1.value;
        };

        const toggleGroup2 = () => {
            showGroup2.value = !showGroup2.value;
        };

        onMounted(async () => {
            const studentStore = useStudentStore();
            const groups = await studentStore.getGroups();
            groups.forEach(group => {
                if (group.is_show) {
                    cardshow.value.push(group);
                } else {
                    cardshidden.value.push(group);
                }
            });
        })

        return {
            showGroup1,
            showGroup2,
            cardshow,
            cardshidden,
            toggleGroup1,
            toggleGroup2
        };
    }
});
</script>