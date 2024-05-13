# https://www.fastprep.io/problems/amazon-review-score
'''
Amazon allows customers to add reviews for the products they bought from their store. The review must follow Amazon's community guidelines in order to be published.

Suppose that Amazon has marked n strings that are prohibited in reviews. They assign a score to each review that denotes how well it follows the guidelines. The score of a review is defined as the longest contiguous substring of the review which does not contain any string among the list of words from the prohibited list, ignoring the case.

Given a review and a list of prohibited string, calculate the review score.

Function Description

Complete the function findReviewScore in the editor.

findReviewScore has the following parameters:

review: a string
string prohibitedWords[n]: the prohibited words
Returns

int: the score of the review
'''
class Solution:
    def amazonReviewScore(self, review: str, prohibitedWords: list[str]) -> int:
        def isContainedProhibitedWord(review, prohibitedWord):
            # O(M)
            for word in prohibitedWord:
                if word.lower() in review.lower():
                    return True

            return False

        left = 0
        result = 0
        for right in range(len(review)):
            while isContainedProhibitedWord(review[left: right + 1], prohibitedWords):
                left += 1

            result = max(result, right - left + 1)

        return result