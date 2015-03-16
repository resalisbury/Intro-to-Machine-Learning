def bayes(p, sensitivity, specificity):
  # sensitivity is the probability test returns true | thing is true. 1 minus the sensitivity is Type I Error.
  # specificity is the probability test returns false | thing is false. 1 minus the specificity is Type II Error.

  # Joint
  true_positives = p * sensitivity
  false_positives = (1 - p) * (1 - specificity)

  # Normalize
  all_positives = true_positives + false_positives

  # Posterior
  return true_positives / all_positives





print(bayes(0.01, 0.9, 0.9))