<template>
    <div class="test-page">
        <div
            class="test-page__title"
        >
            <h2
                contenteditable
                @input="(val) => test.name = val.target.innerText"
            >
                {{ test.name }}
            </h2>

            <TestsCreateModal
                v-if="props.test && props.isCreateFields"
                :test="props.test"
                @saveModal="(val) => scripts.addQuestion(props.test, val)"
                @changeValue="(item, val) => scripts.changeValue(item, val)"
                @changeLabel="(item, val) => scripts.changeLabel(item, val)"
                @deleteOption="(item, val) => scripts.deleteOption(item, val)"
                @addFieldOption="(item) => scripts.addFieldOption(item)"
            />
        </div>

        <div class="test-page__fields">
            <div
                class="test-page__field"
                v-for="(field, index) in props.test.fields"
                :key="field.id"
            >
                <div
                    v-if="!props.isPagePassing"
                    class="test-page__header"
                >
                    <h3
                        class="test-page__position"
                        :class="{ 'test-page__position_required': field.required }"
                    >
                        Вопрос #{{ index + 1 }}
                    </h3>

                    <AppButton class="test-page__delete-field button_clear">
                        <TrashIcon
                            @click.prevent="() => scripts.deleteField(props.test, field.id)"
                        />
                    </AppButton>
                </div>

                <h4
                    v-if="props.isPagePassing"
                    class="test-page__name"
                    :class="{ 'test-page__name_required': field.required }"
                >
                    {{ field.name }}
                </h4>

                <AppTextarea
                    v-else
                    class="test-page__name"
                    :value="field.name"
                    @changeValue="(val) => field.name = val.value"
                />

                <TestPageComponent
                    v-if="!props.isPagePassing && field.type !== 'text' || props.isPagePassing"
                    class="test-page__value"
                    :field="field"
                    :isEdit="props.isEdit"
                    :isPagePassing="props.isPagePassing"
                    @changeValue="(val) => scripts.changeValue(field, val)"
                    @changeLabel="(val) => scripts.changeLabel(field, val)"
                    @deleteOption="(val) => scripts.deleteOption(field, val)"
                    @addFieldOption="() => scripts.addFieldOption(field)"
                />
            </div>
        </div>

        <AppButton
            class="test-page-button"
            @click.prevent="emit('buttonAction')"
        >
            Сохранить
        </AppButton>
    </div>
</template>

<script setup>
    import './TestPage.scss'

    import scripts from "~/components/TestsComponents/scripts.js";

    import TrashIcon from "~/components/AppIcons/Trash.vue";

    import AppTextarea from "~/components/AppInputs/Textarea/Textarea.vue";
    import TestsCreateModal from "~/components/TestsComponents/TestsCreate/TestsCreateModal/TestsCreateModal.vue";
    import TestPageComponent from "~/components/TestsComponents/TestPage/TestPageComponent/TestPageComponent.vue";
    
    const props = defineProps({
        test: {
            type: Object,
            default: {}
        },
        isEdit: {
            type: Boolean,
            default: false
        },
        isCreateFields: {
            type: Boolean,
            default: false
        },
        isPagePassing: {
            type: Boolean,
            default: false
        }
    })

    const emit = defineEmits(['buttonAction'])
</script>