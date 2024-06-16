<template>
    <li class="experience-content__item content-item">
        <div class="content-item__time">
            <p class="content-item__time-date" v-html="timeDate" />
            <p class="content-item__time-total-months">{{ overallTime }}</p>
        </div>

        <div class="content-item__info">
            <div class="content-item__info-company info-company">
                <p class="info-company__name info-name">{{ props.experience.companyInfo.name }}</p>
                <p class="info-company__location">{{ props.experience.companyInfo.location }}</p>
            </div>

            <div class="content-item__info-vacancy info-vacancy">
                <p class="info-vacancy__name info-name">{{ props.experience.positionName }}</p>
                <pre class="info-vacancy__responsibility">{{ props.experience.responsibility }}</pre>
            </div>
        </div>
    </li>
</template>

<script setup>
    import './ResumeExperienceListItem.scss'

    import months from "~/data/months.js";

    const props = defineProps({
        experience: {
            type: Object,
            default: {
                id: 0,
                positionName: 'Не найдено',
                companyInfo: {
                    name: "Не найдено",
                    logo: null,
                    location: "Не найдено",
                    rating: 4.9,
                    subway: null
                },
                timeStart: {
                    month: 2,
                    year: 2023
                },
                timeEnd: {
                    month: 1,
                    year: 2024
                },
                responsibility: 'Не найдено'
            }
        }
    })

    const resumeStore = useResumeStore()

    const timeDate = computed(() => {
        if (props.experience.timeEnd.now) {
            return `
                ${props.experience.timeStart.year} ${months[props.experience.timeStart.month - 1]} - <br>
                По настоящее время
            `
        } else {
            return `
                ${props.experience.timeStart.year} ${months[props.experience.timeStart.month - 1]} - <br>
                ${props.experience.timeEnd.year} ${months[props.experience.timeEnd.month - 1]}
            `
        }
    })

    const overallTime = computed(() => {
        const totalMonth = resumeStore.countMonth(props.experience.timeStart, props.experience.timeEnd)
        return resumeStore.getExperinceTime(totalMonth)
    })
</script>