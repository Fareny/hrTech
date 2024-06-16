export default [
    {
        name: 'Tests',
        questionsCount: 54,
        passingPercentage: 33,
        fields: [
            {
                id: 1,
                name: 'Test',
                type: 'text',
                value: 'test'
            },
            {
                id: 2,
                name: 'Test',
                type: 'textarea',
                value: 'test'
            },
            {
                id: 3,
                name: 'Test',
                type: 'select',
                multiple: false,
                value: 'test',
                options: [
                    {
                        label: 'Test',
                        value: 'test'
                    }
                ]
            },
            {
                id: 4,
                name: 'Test',
                type: 'select',
                multiple: true,
                value: ['test'],
                options: [
                    {
                        label: 'Test',
                        value: 'test'
                    }
                ]
            },
            {
                id: 5,
                name: 'Test',
                type: 'radio',
                value: 'test',
                options: [
                    {
                        label: 'Test',
                        value: 'test'
                    }
                ]
            },
            {
                id: 6,
                name: 'Test',
                type: 'checkbox',
                value: ['test'],
                options: [
                    {
                        label: 'Test',
                        value: 'test'
                    }
                ]
            },
        ],
        answers: [
            {
                id: 1,
                noAnswer: false,
                value: 'test'
            },
            {
                id: 2,
                noAnswer: true,
                value: null
            },
            {
                id: 3,
                noAnswer: false,
                value: 'test',
            },
            {
                id: 4,
                noAnswer: false,
                value: ['test'],
            },
            {
                id: 5,
                noAnswer: false,
                value: 'test',
            },
            {
                id: 6,
                noAnswer: false,
                value: ['test'],
            },
        ]
    }
]