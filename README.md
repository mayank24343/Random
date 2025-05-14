# randompkg

`randompkg` is a lightweight Python module implementing a custom pseudo-random number generator (PRNG) and a set of common random utilities and probability distributions — perfect for educational use or quick experimentation.

## Features

### Core PRNG
- Linear Congruential Generator (LCG) with customizable parameters
- Seed control, reproducibility

### Random Utilities
- `random()`, `randint()`, `randrange()`
- `choice()` with and without replacement
- `shuffle()` and `shufflestring()`

### Probability Distributions
- Discrete: Bernoulli, Binomial, Geometric, Pascal, Poisson
- Continuous: Uniform, Gaussian (Normal), Exponential

## Module Structure

- `MYpRNG.py`: Core LCG-based pseudo-random number generator
- `MYRandom.py`: Utility functions built on top of the PRNG
- `MYProbability.py`: Probability distributions and random sampling

## Documentation

### To Import
`import randompkg`

### MYpRNG.py

| Function           | Description                         |
| ------------------ | ----------------------------------- |
| `pRNG()`           | Get next pseudo-random number (int) |
| `setSeed(s)`       | Set the internal seed               |
| `setMultiplier(m)` | Set LCG multiplier                  |
| `setIncrement(i)`  | Set LCG increment                   |
| `setModulo(m)`     | Set LCG modulo                      |

### MYRandom.py

| Function                             | Description                             |
| ------------------------------------ | --------------------------------------- |
| `random()`                           | Float in \[0, 1)                        |
| `randrange(start, stop)`             | Random int with optional step           |
| `randint(a, b)`                      | Random int between a and b              |
| `choice(seq, n=1, replacement=True)` | Choose `n` items from sequence          |
| `shuffle(seq)`                       | Shuffle list in-place                   |
| `shufflestring(string)`              | Return a shuffled version of the string |

### MYProbability.py

| Function                | Description                          |
| ----------------------- | ------------------------------------ |
| `uniform(a, b)`         | Uniform float between a and b        |
| `uniformSeq(n, a, b)`   | Uniform sequence                     |
| `bernoulli(p)`          | 0 or 1 with prob `p`                 |
| `bernoulliseq(n, p)`    | List of Bernoulli trials             |
| `binomial(n, p)`        | Binomial sample                      |
| `binomialSeq(n, N, p)`  | List of Binomial samples             |
| `geometric(p)`          | Geometric sample                     |
| `geometricSeq(n, p)`    | List of Geometric samples            |
| `pascal(N, p)`          | Pascal (Negative Binomial) sample    |
| `pascalSeq(n, N, p)`    | List of Pascal samples               |
| `poisson(λ)`            | Poisson sample (via Binomial approx) |
| `poissonSeq(n, λ)`      | List of Poisson samples              |
| `gaussian(μ, σ²)`       | Gaussian (normal) sample             |
| `gaussianSeq(n, μ, σ²)` | List of Gaussian samples             |
| `exponential(λ)`        | Exponential sample                   |
| `exponentialSeq(n, λ)`  | List of Exponential samples          |

## Future Work

- Random Colours Generator 
- Expand on pRNG used 
- Option for custom distribution in `MYProbability.py`
