<template>
    <div ref="editor"></div>
</template>
<script>
import Quill from "quill";
import "quill/dist/quill.core.css";
import "quill/dist/quill.bubble.css";
import "quill/dist/quill.snow.css";

export default {
    props: {
        content: {
            type: String,
            default: '',
        },
    },
    data() {
        return {
            editor: null,
        };
    },
    mounted() {
        var _this = this;

        this.editor = new Quill(this.$refs.editor, {
            modules: {
                toolbar: [
                    [
                        {
                            header: [1, 2, 3, 4, false],
                        },
                    ],
                    ["bold", "italic", "underline", "link"],
                ],
            },
            theme: "snow",
            formats: ["bold", "underline", "header", "italic", "link"],
            placeholder: "Type something in here!",
        });
        this.editor.root.innerHTML = this.content;
        this.editor.on("text-change", function () {
            return _this.update();
        });
    },
    watch: {
        content(newContent) {
            if (this.editor.root.innerHTML !== newContent) {
                this.editor.root.innerHTML = newContent;
            }
        },
    },
    methods: {
        update: function update() {
            this.$emit(
                "update:modelValue",
                this.editor.getText() ? this.editor.root.innerHTML : ""
            );
        },
    },
};
</script>