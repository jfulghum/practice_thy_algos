/*

if a user is in the given policy or any nested subpolicy, they have access to all the resources in the parent policy(ies)

policy: {
   policyID: string,
   users: [UserID],[]
   resources: [ResourceID],[]
   subPolicies: [Policy]
}

hasAccess(userID, resourceID) => boolean

{
  policyID: 'policy1',
  users: ['user1'],
  resources: ['resource1'],
  subPolicies: ['policy2']
}

{
  policyID: 'policy2',
  users: ['user2'],
  resources: ['resource2'],
  subPolicies: ['policy1']
}

traverse from every node to check for parents/nodes of userId

one of these nodes needs resourceID

const graph = [
  {
    policyID: string,
    users: [UserID],[]
    resources: [ResourceID],[]
    subPolicies: [Policy]
  }
]

iterate through all policies
  for a given policy: check if targetResource exists
    if yes
      check if targetUser exists
        if yes => return true
        if no => are there subPolicies?
          if yes => recurse


*/

const graph = [];

const hasAccess = (targetUserID, targetResourceID) => {
  const processedPolicies = {};
  
  for (let i = 0; i < graph.length; i++) {
    const curPolicy = graph[i];
    const {policyID, users, resources, subPolicies} = curPolicy;

    const hasResource = resources.includes(targetResourceID);

    let foundUser;

    if (hasResource) {
      foundUser = findUser(curPolicy);
    }

    processedPolicies[policyID] = true;

    if (foundUser) {
      return true;
    }
  }

  const findUser = ({policyID, users, subPolicies}) => {
    if (policyID in processedPolicies) return false
    processedPolicies[policyID] = true;

    if (users.includes(targetUserID)) {
      return true;
    }

    let foundUser = false;

    subPolicies.forEach(subPolicy => foundUser || findUser(subPolicy));
    
    return foundUser;
  }
}
