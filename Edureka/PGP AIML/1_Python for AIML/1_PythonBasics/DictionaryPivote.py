class DictionaryPivote:
    def transform(self, data:dict):
        transformed_data = {}
        for subject, students in data.items():
            for key, value in students.items():
                if key not in transformed_data:
                    transformed_data[key] = []
                transformed_data[key].append(value)
        for key, value in transformed_data.items():
            marks = transformed_data[key]
            transformed_data[key] = sum(marks)/len(data.keys())
        return transformed_data
if __name__ == '__main__':
    print(DictionaryPivote().transform(
        {
            'English':{'Sam':60, 'Jackson': 74, 'Ahree': 85},
            'History':{'Gloria':83, 'Sam': 65, 'Isla': 78, 'Aron': 72, 'Gray':61},
            'Geography': {'Jackson': 92, 'Gloria': 95, 'Isla': 82, 'Aron':75, 'Ahree': 76},
            'Mathematics': {'Sam': 99, 'Gloria': 74, 'Jackson': 89, 'Ahree': 85, 'Gray': 95},
            'Science': {'Sam': 89, 'Aron': 82, 'Gray': 78, 'Isla': 93, 'Ahree': 87},
        }
    ))
