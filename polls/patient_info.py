import json


if __name__ == '__main__':
    patient_dict = {}
    patient_info = {}

    patient = {"age": 10, "sex": "female", "bp": 100, "temp": 37, "bpm": 20}
    patient_queue = {'rank': 4, "queue": 2, "wait_time": 10}

    patient_dict['user1'] = patient
    patient_info ['user1'] = patient_queue

    with open('patients.json', 'w') as outfile:
        json.dump(patient_dict, outfile)

    with open('patients_info.json', 'w') as outfile:
        json.dump(patient_info, outfile)