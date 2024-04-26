#!/bin/bash
# Flag definition
org_id=""
location="eastus"
include_groups=false
resource_group_name=""

print_usage() {
  echo "This setup script will install the Open Edu Analytics base architecture and the example Contoso package with test data sets."
  echo ""
  echo "Invoke this script like this:  "
  echo "    setup.sh -o <org_id>"
  echo "where org_id is a suffix representing your organization (eg, CISD3). This value must be 12 characters or less (consider using an abbreviation) and must contain only letters and/or numbers."
  echo ""
  echo "By default, the Azure resources will be provisioned in the East US location."
  echo "If you want to have the resources provisioned in an alternate location, invoke the script like this: "
  echo "    setup.sh -o <org_id> -l <location>"
  echo "where org_id is a suffix for your organization (eg, CISD3), and location is the abbreviation of the desired location (eg, eastus, westus, northeurope)."
  echo ""
  echo "By default, the Azure resource group will be provisioned as rg-oea-<org_id>."
  echo "If you want to have the resource group provisioned with an alternate name, invoke the script like this: "
  echo "    setup.sh -o <org_id> -r <resource_group_name>"
  echo "where org_id is a suffix for your organization (eg, CISD3), and resource_group_name is the name of the resource group that follows your internal naming convention."
  echo ""
  echo "If you have Global Admin rights for the tenant associated with your Azure subscription, and you want to have the script setup security groups to facilitate the management of role based access control, you can invoke the script like this:"
  echo "You can opt to create a set of resources (eg, for a test env) without setting up the security groups like this:"
  echo "    setup.sh -o <org_id> -i"
  echo "where org_id is a suffix for your organization (eg, CISD3), and -i specifies that security groups should be created."
  exit 1
}

datetime=$(date "+%Y%m%d_%H%M%S")
logfile="oea_setup_${datetime}.log"
exec 3>&1 1>>${logfile} 2>&1

# The assumption here is that this script is in the base path of the OpenEduAnalytics project.
oea_path=$(dirname $(realpath $0))

# Set Flags
while getopts ":o:l:ir:" flag; do
  case "${flag}" in
    o) 
      echo "argument -o called with value ${OPTARG}"
      org_id=${OPTARG} 
      ;;
    l) 
      echo "argument -l called with value ${OPTARG}"
      location=${OPTARG} 
      ;;
    i) 
      echo "flag -i is enabled"
      include_groups=true
      ;;
    r) 
      echo "argument -r called with value ${OPTARG}"
      resource_group_name=${OPTARG} 
      ;;
    :)                                    
      echo "Error: argument -${OPTARG} requires a value"
      echo ""
      print_usage
      ;;
    *) 
      echo "Error: argument -${OPTARG} is not valid"
      echo ""
      print_usage
      ;;
  esac
done

# If org_id was not passed as an input argument, then display usage instructions and exit script
if test -z "$org_id" 
then
  print_usage
fi

