#!/usr/bin/env python
# encoding: utf-8

"""Functions for manipulating data from 23 and me
"""

import collections
import operator


def snp_to_location_and_genotype(data, snp):
    """Given a snp name, return its location and all the genotypes found there"""
    all_snps = data.searchSNP(snp)
    some_file = all_snps[0][0]
    return data.Data[some_file][snp][0], int(data.Data[some_file][snp][1]), all_snps


def sorted_snps_by_chromosome(data):
    """Group snps by chromosome and sort them by position"""
    chromosomes = collections.defaultdict(list)
    for snp in data.Intersection:
        result = snp_to_location_and_genotype(data, snp)
        if result[0].isdigit():
            chromosomes[result[0]].append(result)
    for k, v in chromosomes.items():
        v.sort(key=operator.itemgetter(1))
    return chromosomes


def genotypes_at_location(location):
    return [genotype[1] for genotype in location[2]]


def allele_frequencies(genotype):
    bases = []
    for pair in genotype:
        bases.append(pair[0])
        bases.append(pair[1])
    counts = collections.Counter(bases)
    total = float(len(genotype) * 2)
    frequencies = [(count[0], count[1] / total) for count in counts.most_common()]
    return frequencies


def pair_histogram(genotype_a, genotype_b):
    counts = collections.Counter()
    for i in range(len(genotype_a)):
        pair_genotype = genotype_a[i] + genotype_b[i]
        counts[pair_genotype] += 1
    return counts


def are_correlated(genotype_a, genotype_b):
    """Return two if two loci are correlated"""

    # TODO This logic is not correct, but a start. Please properly implement correlation.
    hist = pair_histogram(genotype_a, genotype_b)
    total = len(genotype_a)
    # if the most common pair value appears more than 80% of time, then they are correlated
    return hist.most_common(1)[0][1] > (total * 0.8)


def discard_correlated_snps(snps_on_chromosome):
    """Return snps that we want to keep for the analysis"""
    discard_set = set()
    for i, location_a in enumerate(snps_on_chromosome):
        genotypes_a = genotypes_at_location(location_a)
        start = min(i + 1, len(snps_on_chromosome) - 1)
        end = min(i + 51, len(snps_on_chromosome))
        for j in range(start, end):
            location_b = snps_on_chromosome[j]
            genotypes_b = genotypes_at_location(location_b)
            if are_correlated(genotypes_a, genotypes_b):
                discard_set.add(i)
                break
    culled_snps = []
    for i, location in enumerate(snps_on_chromosome):
        if not i in discard_set:
            culled_snps.append(location)
    return culled_snps
