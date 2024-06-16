export default {
    getFieldComponent(type) {
        switch (type) {
            case 'text':
                return markRaw(defineAsyncComponent(() => import('@/components/AppInputs/Textarea/Textarea.vue')))
            case 'radio':
                return markRaw(defineAsyncComponent(() => import('@/components/TestsComponents/TestsCheckbox/TestsCheckbox.vue')))
            case 'checkbox':
                return markRaw(defineAsyncComponent(() => import('@/components/TestsComponents/TestsCheckbox/TestsCheckbox.vue')))
        }
    },

    generateFieldId(arr) {
        return arr.length > 0 ? Math.max(...arr.map(item => item.id)) + 1 : 1
    },

    changeValue(item, val) {
        if (item.type === 'checkbox') {
            if (val.value) {
                item.value.push(val.id)
            } else {
                item.value = item.value.filter(el => el !== val.id)
            }
        } else if (item.type === 'radio') {
            item.value = val.id
        } else {
            item.value = val.value
        }
    },

    changeLabel(item, val) {
        item.options.find(el => el.value === val.id).label = val.value
    },

    deleteOption(item, val) {
        item.options = item.options.filter(el => el.value !== val.id)
        item.value = item.value.filter(el => el !== val.id)
    },

    addFieldOption(item) {
        const optionId = item.options.length > 0 ? Math.max(...item.options.map(el => +el.value.slice(-1))) + 1 : 0

        item.options.push({
            label: 'Новая опция',
            value: `${item.id}_${optionId}`
        })
    },

    addQuestion(item, questiton) {
        questiton.id = this.generateFieldId(item.fields)

        item.fields.push(toRaw(questiton))
    },

    deleteField(item, fieldId) {
        item.fields = item.fields.filter(el => el.id !== fieldId)
    }
}