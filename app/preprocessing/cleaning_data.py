def preprocess(requested_data):

	property_type_remap = {"APARTMENT": 0, "HOUSE": 1, "OTHERS": 2}
	building_state_remap = {"NEW": 4, "GOOD": 3, "TO RENOVATE": 2, "JUST RENOVATED": 1, "TO REBUILD": 0}

	

	if "property_type" in requested_data:
		requested_data["property_type"] = property_type_remap[requested_data["property_type"]]
	else:
		return "error"

	if "area" not in requested_data:
		return "error"

	if "rooms_number" not in requested_data:
		return "error"

	if "zip_code" not in requested_data:
		return "error"


	requested_data["building_state"] = building_state_remap[requested_data["building_state"]]

	if requested_data["garden"] == True:
		requested_data["garden"] = 1
	else:
		requested_data["garden"] = 0

	if requested_data["equipped_kitchen"] == True:
		requested_data["equipped_kitchen"] = 1
	else:
		requested_data["equipped_kitchen"] = 0

	if requested_data["swimming_pool"] == True:
		requested_data["swimming_pool"] = 1
	else:
		requested_data["swimming_pool"] = 0

	if requested_data["furnished"] == True:
		requested_data["furnished"] = 1
	else:
		requested_data["furnished"] = 0

	if requested_data["open_fire"] == True:
		requested_data["open_fire"] = 1
	else:
		requested_data["open_fire"] = 0

	if requested_data["terrace"] == True:
		requested_data["terrace"] = 1
	else:
		requested_data["terrace"] = 0

	return requested_data


