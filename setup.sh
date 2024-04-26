source $oea_path/framework/infrastructure/bash/set_names.sh $org_id $resource_group_name

subscription_id=$(az account show --query id -o tsv)

# Verify that the specified org_id is not too long and doesn't have invalid characters.
# The length is constrained by the fact that the synapse workspace name must be <= 24 characters, and our naming convention requires that it start with "syn-oea-".
if [[ ${#org_id} -gt 16 || ! $org_id =~ ^[a-zA-Z0-9]+$ ]]; then
  echo "Invalid suffix: $org_id"
  echo "Invalid suffix: $org_id" 1>&3
  echo "The chosen suffix must be less than 12 characters, and must contain only letters and numbers."
  echo "The chosen suffix must be less than 12 characters, and must contain only letters and numbers." 1>&3
  exit 1
fi

# Verify that the user has the Owner role assignment
roles=$(az role assignment list --subscription $subscription_id --query [].roleDefinitionName -o tsv)
if [[ ! " ${roles[@]} " =~ "Owner" ]]; then
  echo "You do not have the role assignment of Owner on this subscription."
  echo "You do not have the role assignment of Owner on this subscription." 1>&3
  echo "For more info, click here -> https://github.com/microsoft/OpenEduAnalytics/wiki/Setup-Tips#error-must-have-role-assignment-of-owner-on-subscription"
  echo "For more info, click here -> https://github.com/microsoft/OpenEduAnalytics/wiki/Setup-Tips#error-must-have-role-assignment-of-owner-on-subscription" 1>&3
  exit 1
fi

echo "--> Setting up OEA (logging detailed setup messages to $logfile)"
echo "--> Setting up OEA (logging detailed setup messages to $logfile)" 1>&3

