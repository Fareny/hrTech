<template>
    <AppSection class="main-content__filters section_padding-small">
        <SectionTitle>Фильтры</SectionTitle>

        <AppDropdown
            class="filter"
            v-for="filter in vacancyStore.filters"
            :key="filter.id"
            :startOpen="true"
        >
            <template #summary>
                <span>{{ filter.name }}</span>
                <ArrowDown />
            </template>

            <template #content>
                <fieldset>
                    <DropdownItem
                        v-for="option in filter.options"
                        class="filter__item"
                        :key="option.id"
                        :class="option.isCustomValue ? 'filter__item_custom' : ''"
                    >
                        <AppCheckbox
                            class="filter__item-checkbox"
                            :id="option.id"
                            :type="filter.type"
                            :itemName="`${filter.id}_${filter.type}`"
                            @changeValue="(val) => selectFilterItem(val, filter.id)"
                        >
                            <span class="filter__item-name">{{ option.name }}</span>
                        </AppCheckbox>
                        <span class="filter__item-count">{{ option.count }}</span>

                        <AppInput
                            v-if="option.isCustomValue"
                            class="filter__item-input"
                            placeholder="от"
                            :value="option.customValue"
                            @changeValue="(val) => option.customValue = val.value"
                        />
                    </DropdownItem>
                </fieldset>
            </template>
        </AppDropdown>
        <AppButton class="filter__apply" :disabled="true">Применить</AppButton>
        <span class="filter__reset" @click="$emit('search', {})">Сбросить</span>
    </AppSection>
</template>

<script setup>
    import './Filters.scss'

    import AppSection from "~/components/AppSection/AppSection.vue";
    import AppDropdown from "~/components/AppDropdown/AppDropdown.vue";
    import AppInput from '~/components/AppInputs/Input/Input.vue';
    import SectionTitle from "~/components/AppSection/SectionTitle/SectionTitle.vue";
    import DropdownItem from "~/components/AppDropdown/DropdownItem/DropdownItem.vue";
    import AppCheckbox from "~/components/AppInputs/Checkbox/Checkbox.vue";
    import ArrowDown from "~/components/AppIcons/ArrowDown.vue";

    const vacancyStore = useVacancyStore()

    const selectFilterItem = (item, filterId) => {
        const currentFilter = vacancyStore.filters.find(filter => filter.id === filterId)
        const currentOption = currentFilter.options.find(option => option.id === item.id)
        currentOption.selected = item.value
    }
</script>