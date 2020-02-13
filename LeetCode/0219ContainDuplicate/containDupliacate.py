class Sulotion(object):
    def containNearbyDuplicate(self,nums,k):
        dictIndex={}
        for i in range(len(nums)):
            if dictIndex.has_key(nums[i]):
                if i-dictIndex[nums[i]]<=k:
                    return True
            dictIndex[nums[i]]=i
        return False

