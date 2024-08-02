<template>
    <div class="editor">
        <div class="row d-flex justify-content-center">
            <div class="col-lg-7">
                <QuillEditor :toolbar="toolbarOptions" v-model="content" :options="editorOption"
                    @update:content="handleContentUpdate" :modules="modules" />
            </div>
            <!-- <div class="col-lg-7 d-flex justify-content-end my-4">
                <a-button @click="save"></a-button>
            </div> -->
        </div>

    </div>
</template>

<script>
import 'quill/dist/quill.snow.css'
import { ref, watch } from 'vue'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import { QuillDeltaToHtmlConverter } from 'quill-delta-to-html'

import teacherService from "../../apis/modules/teacher.js";


export default {
    components: {
        QuillEditor,

    },
    props: ['response'],

    setup(props, context) {

        const content = ref('')

        const editorOption = ref({
            debug: 'info',
            placeholder: 'Nhập câu hỏi...',
            theme: 'snow',
            debug: false,
        })

        const toolbarOptions = [
            { 'header': [1, 2, 3, 4, 5, 6, false] },
            'bold', 'italic', 'underline', 'strike', 'link', 'code',
            { 'color': [] }, { 'background': [] },
            { 'list': 'ordered' }, { 'list': 'bullet' },
            { align: [] },

        ]

        // const modules = {
        //     name: 'imageUploader',
        //     module: ImageUploader,
        //     options: {
        //         upload: file => {
        //             return new Promise((resolve, reject) => {
        //                 const formData = new FormData()
        //                 formData.append('file', file)

        //                 teacherService.uploadImage(formData, props.response)
        //                     .then(res => {
        //                         resolve(res)
        //                     })
        //                     .catch(err => {
        //                         reject('Upload failed')
        //                         console.error('Error:', err)
        //                     })
        //             })
        //         }
        //     }
        // }


        let delta = undefined

        watch(content, () => {
            delta = content.value.ops
        })


        const renderHTML = ref('')

        const handleContentUpdate = (newContent) => {
            var deltaOps = newContent
            var converter = new QuillDeltaToHtmlConverter(deltaOps.ops, {})
            renderHTML.value = converter.convert()
            context.emit('add-question', renderHTML.value)
        }

        // const save = () => {
        //     context.emit('add-question', renderHTML.value)
        // }

        return {
            //  save,
            handleContentUpdate,
            renderHTML,
            toolbarOptions,
            content,
            editorOption,
            //  modules,
        }
    }
}


</script>
<style scoped>
* {
    box-sizing: border-box;
}

</style>

<style>
.ql-toolbar {
    position: sticky;
    top: 84px;
    background-color: var(--color-white);
    z-index: 2;
}

</style>