import math
from collections import Counter

# equal probability for both coins A and B
probability_of_coin_being_picked = 0.5


def read_observation_file(filename):
    with open(filename, 'rb') as infile:
        total_observations = infile.readlines()
    return total_observations


def calculate_counts(observation):
    return Counter(observation.upper())


def calculate_probability_of_observation_given_coin(prob_coin, number_of_heads, number_of_tails):
    # P(S|A) for binomial distribution
    return math.pow(prob_coin, number_of_heads) * math.pow(1 - prob_coin, number_of_tails)


def calculate_probability_of_coin_given_observation(prob_coin_a, prob_coin_b, number_of_heads, number_of_tails):
    prob_s_given_a = calculate_probability_of_observation_given_coin(prob_coin_a, number_of_heads, number_of_tails)
    prob_s_given_b = calculate_probability_of_observation_given_coin(prob_coin_b, number_of_heads, number_of_tails)
    probability = prob_s_given_a * probability_of_coin_being_picked / (
            prob_s_given_a * probability_of_coin_being_picked + prob_s_given_b * probability_of_coin_being_picked)
    return probability, (1 - probability)


def main():
    iteration = 0
    prob_a_given_observation = 0.6
    prob_b_given_observation = 0.5
    number_of_heads = [5, 9, 8, 4, 7]
    number_of_tails = [5, 1, 2, 6, 3]

    while iteration != 30:
        sum_ha = 0
        sum_hb = 0
        sum_ta = 0
        sum_tb = 0
        for head, tail in zip(number_of_heads, number_of_tails):
            prob_a, prob_b = calculate_probability_of_coin_given_observation(
                prob_a_given_observation, prob_b_given_observation, head, tail)
            print(prob_a, prob_b, head * prob_a, tail * prob_a, head * prob_b, tail * prob_b)
            print('\n')
            sum_ha += head * prob_a
            sum_ta += tail * prob_a
            sum_hb += head * prob_b
            sum_tb += tail * prob_b
        print("After {0} iterations:".format(iteration + 1))
        prob_a_given_observation = sum_ha / (sum_ha + sum_ta)
        prob_b_given_observation = sum_hb / (sum_hb + sum_tb)
        print(prob_a_given_observation, prob_b_given_observation)
        iteration += 1


if __name__ == "__main__":
    main()
