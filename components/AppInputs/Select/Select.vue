<template>
    <div
        class="select"
        :class="{'select_disabled': props.disabled}"
    >
        <InputLabel
            v-if="props.name !== ''"
        >
            {{ props.name }}
        </InputLabel>

        <AppDetails
            class="select__details"
            ref="detailsRef"
            :closeByClick="false"
            :class="props.isMultiple ? 'select__details_multiply' : ''"
            :disabled="props.disabled"
            @clickOutside="() => emit('clickOutside', true)"
        >
            <template #summary>
                <AppInput
                    ref="inputRef"
                    :value="activeOptions == null ? null : activeOptions.label"
                    :disabled="!props.isFiltered"
                    :enabledAutocomplete="false"
                    @changeValue="(data) => callAction({action: 'searchOptions', value: data.value})"
                    @mousedown="() => callAction({action: 'showContent', value: true})"
                    @keydown.space="(event) => {event.preventDefault(); callAction({action: 'searchOptions', value: event.target.value + ' '})}"
                >
                    <div class="select__active-option active-option" v-show="props.isMultiple || ([null, undefined].includes(search) || search === '')">
                        <template v-if="props.isMultiple && activeOptions != null">
                            <div class="select__active-option-tab" v-for="tab in activeOptions">
                                {{ tab.label }}

                                <TrashIcon
                                    @click="(event) => callAction({action: 'changeValue', value: tab.value, event: event})"
                                />
                            </div>

                            <div class="active-option__mirror">
                                <div class="form-item__mirror">
                                    {{ search }}
                                </div>
                                <input
                                    ref="mirrorRef"
                                    type="text"
                                    :value="search"
                                    :disabled="!props.isFiltered"
                                    @input="(e) => callAction({action: 'searchOptions', value: e.target.value})"
                                >
                            </div>
                        </template>
                        <template v-else>
                            {{ activeOptions == null ? nullOption.label : activeOptions.label }}
                        </template>
                    </div>
                </AppInput>
            </template>
            <template #content>
                <DetailsItem v-show="props.isHaveNullOption && !props.isMultiple || options.length === 0" @click="() => callAction({action: 'changeValue', value: null})">
                    Не выбрано
                </DetailsItem>
                <DetailsItem
                    class="details-option__root"
                    v-for="option in options"
                    :class="option.value === activeOptions.value || multiplyValues.includes(option.value) ? 'details__content-item_active' : ''"
                    @click="() => callAction({action: 'changeValue', value: option.value})"
                >
                    <div class="details__content-item__text">
                        {{ option.label }}
                        <CheckIcon />
                    </div>
                </DetailsItem>
            </template>
        </AppDetails>
    </div>


</template>

<script setup>
    import './Select.scss'

    import AppDetails from '~/components/AppDetails/AppDetails.vue';
    import AppInput from '~/components/AppInputs/Input/Input.vue';
    import DetailsItem from '~/components/AppDetails/DetailsItem/DetailsItem.vue';

    import TrashIcon from '~/components/AppIcons/Trash.vue';
    import CheckIcon from "~/components/AppIcons/Check.vue";
    import InputLabel from "~/components/AppInputs/InputLabel/InputLabel.vue";

    const props = defineProps({
        id: {
            default: 0,
            type: [String, Number]
        },
        name: {
            default: '',
            type: String
        },
        value: {
            default: '',
            type: String
        },
        options: {
            default: [],
            type: Array
        },
        isMultiple: {
            default: false,
            type: Boolean
        },
        isHaveNullOption: {
            default: false,
            type: Boolean
        },
        isFiltered: {
            default: false,
            type: Boolean
        },
        disabled: {
            default: false,
            type: Boolean
        }
    })

    const emit = defineEmits([
        'changeValue',
        'clickOutside'
    ])

    const detailsRef = ref(null)
    const inputRef = ref(null)
    const mirrorRef = ref(null)
    const nullOption = {
        label: "Не выбрано",
        value: null
    }

    const options = ref([])
    const search = ref(null)
    const backupOptions = ref([])
    const multiplyValues = ref([])
    const activeOptions = ref(props.isMultiple ? [] : nullOption)

    // Действия с автокомплитом
    const callAction = async (data) => {

        // Открытие/скрытие всплывающего окна
        const showContent = (state) => {
            if (state) {
                setTimeout(() => {
                    if (props.isMultiple) {
                        mirrorRef.value.focus()
                    } else {
                        inputRef.value.inputRef.focus()
                    }
                }, 10);
            } else {
                detailsRef.value.detailsRef.removeAttribute('open')
            }
        }

        // Получение опций
        const getOptions = async () => {
            // Проверка на пустой объект
            const isEmpty = (obj) => {
                for (const prop in obj) {
                    if (Object.hasOwn(obj, prop)) {
                        return false;
                    }
                }
                return true;
            }

            const localOptions = props.options == null ? [] : props.options.filter(p => p != null && typeof p == 'object' && !Array.isArray(p) && !isEmpty(p))
            options.value = JSON.parse(JSON.stringify(localOptions))
        }

        // Установка выбранной опции
        const setActiveOptions = async (value) => {
            search.value = ''

            // Нахождение выбранной опции
            const findOption = (value) => {
                const findedOption = options.value == null ? null : options.value.find(option => option.value === value)
                if (Array.isArray(value) || [null, undefined].includes(findedOption)) {
                    return nullOption
                } else {
                    return findedOption
                }
            }

            if (props.isMultiple) {
                const data = []

                for (let item of multiplyValues.value) {
                    data.push(findOption(item))
                }

                activeOptions.value = data.filter(option => option.value != null)
            } else {
                activeOptions.value = findOption(value)
            }
        }

        // Поиск опций
        const searchOptions = (value) => {
            search.value = value
            options.value = backupOptions.value.filter(option => option.label.toLowerCase().includes(search.value.toLowerCase()))

            if (!detailsRef.value.detailsRef.hasAttribute('open')) {
                detailsRef.value.detailsRef.setAttribute('open', true)
            }
        }

        // Изменить значение поля
        const changeValue = (value, event = null) => {
            search.value = null

            if (props.isFiltered) {
                options.value = backupOptions.value
            }

            if (props.isMultiple) {
                if (multiplyValues.value.includes(value)) {
                    multiplyValues.value = multiplyValues.value.filter(option => option !== value)
                    showContent(true)
                } else {
                    multiplyValues.value.push(value)
                }

                setTimeout(() => {
                    mirrorRef.value.focus()
                }, 10);

                if (value === null) return
                emit('changeValue', {
                    id: props.id,
                    value: multiplyValues.value
                })
            } else {
                showContent(false)

                if (value === null) return
                emit('changeValue', {
                    id: props.id,
                    value: value
                })
            }

            setActiveOptions(value)

        }

        switch (data.action) {
            // Отображение всплывающего окна
            case 'showContent':
                showContent(data.value)
                break;

            // Установка выбранной опции
            case 'setActiveOptions':
                await setActiveOptions(data.value)
                break;

            // Поиск опций
            case 'searchOptions':
                searchOptions(data.value)
                break;

            // Изменить значение поля
            case 'changeValue':
                changeValue(data.value, data.event)
                break;

            // Получение опций
            case 'getOptions':
                await getOptions()
                break;

            default:
                break;
        }
    }

    onMounted(async () => {
        await callAction({
            action: 'getOptions',
            value: null
        })
        backupOptions.value = JSON.parse(JSON.stringify(options.value))

        if (props.isMultiple) {
            if ([null, undefined].includes(props.value) || typeof props.value == 'string') {
                multiplyValues.value = []
            } else {
                multiplyValues.value = [...new Set(props.value)]
            }
        }

        await callAction({
            action: 'setActiveOptions',
            value: props.value
        })
    })

    watch(() => props.options, () => {
        callAction({
            action: 'getOptions',
            value: null
        })
    })

    watch(() => props.value, () => {
        if (props.isMultiple) {
            if ([null, undefined].includes(props.value) || typeof props.value == 'string') {
                multiplyValues.value = []
            } else {
                multiplyValues.value = [...new Set(props.value)]
            }
        }

        callAction({
            action: 'getOptions',
            value: null
        })

        callAction({
            action: 'setActiveOptions',
            value: props.value
        })
    })
</script>