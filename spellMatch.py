
import Levenshtein as lev #Package which helps calculate edit distance between two strings


# class object which can be configured with a threshold 
#to calculate and check if two strings are similar
class stringDistanceMatchTools:
    def __init__(self, Thereshold):
        self.distanceThereshold = Thereshold
    
    # method takes in 2 string inputs 
    # checks similarity and outputs a boolean 
    def levenshtein_match(self, src, tgt):
        distance = lev.distance(src, tgt)
        dist_ratio = distance / len(tgt)
        if dist_ratio < self.distanceThereshold:
            return True
        else:
            return False

# class object which inherits stringDistanceMatchTools methods 
class matcher(stringDistanceMatchTools):
    def __init__(self, threshold):
        stringDistanceMatchTools.__init__(self, threshold)
    
    def distanceMatch(self, src, tgt):
      lev_result = stringDistanceMatchTools.levenshtein_match(self, src, tgt)
      if lev_result:
        return True
      else:
        return False

    def stringMatch(self, src, tgt):
        if src == tgt:
            return True
        else:
            return False

    def findMatch(self, src, tgt):
        try:
            result = self.stringMatch(src, tgt)
            if not result:
                    result = self.distanceMatch(src, tgt)
        except Exception as e:
            result = False
        return result