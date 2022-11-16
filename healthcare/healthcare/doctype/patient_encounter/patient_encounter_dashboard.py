from frappe import _


def get_data():
	return {
<<<<<<< HEAD
		"fieldname": "encounter",
		"non_standard_fieldnames": {
			"Patient Medical Record": "reference_name",
			"Inpatient Medication Order": "patient_encounter",
			"Nursing Task": "reference_name",
		},
		"transactions": [
			{"label": _("Records"), "items": ["Vital Signs", "Patient Medical Record"]},
			{"label": _("Orders"), "items": ["Inpatient Medication Order", "Nursing Task"]},
=======
		'fieldname': 'encounter',
		'non_standard_fieldnames': {
			'Patient Medical Record': 'reference_name',
			'Inpatient Medication Order': 'patient_encounter',
			'Service Request': 'order_group'
		},
		'transactions': [
			{
				'label': _('Records'),
				'items': ['Vital Signs', 'Patient Medical Record']
			},
			{
				'label': _('Orders'),
				'items': ['Inpatient Medication Order', 'Service Request']
			}
>>>>>>> origin/hsr-insurance-wip
		],
		"disable_create_buttons": ["Inpatient Medication Order"],
	}
