class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        local_name = []
        domain_name = []
        ensemble = set()
        for i in emails:
            local_name.append(i.split('@')[0])
            domain_name.append(i.split('@')[1])

        for l in range(len(local_name)):
            local_name[l] = local_name[l].split('+')[0].replace('.', '')

        for k, v in zip(local_name, domain_name):
            # print(k, v)
            ensemble.add(k + '@' + v)
        # print(ensemble)
        return len(ensemble)