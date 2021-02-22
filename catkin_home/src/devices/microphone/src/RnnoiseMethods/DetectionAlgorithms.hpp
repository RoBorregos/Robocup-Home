#ifndef RNNOISE_METHODS__DETECTION_ALGORITHMS_HPP
#define RNNOISE_METHODS__DETECTION_ALGORITHMS_HPP

#include <cstdint>

namespace rnnoise_methods {
namespace detection_algorithms {
constexpr int NUMBER_FRAMES_RNNOISE = 480;
constexpr long SAMPLE_RATE = 48000L;
constexpr int MS_IN_A_CHUNK = (NUMBER_FRAMES_RNNOISE * 1000L) / SAMPLE_RATE;

// This should be used as the limit of seconds to record.
constexpr int SECONDS_ACTUAL_RECORDING = 10;
constexpr long ACTUAL_RECORDING_BUFFER_SIZE = SECONDS_ACTUAL_RECORDING * SAMPLE_RATE;


// TODO: Use this types in the declarations of functions to ensure the type correctness.
/*
 * The method should handle cases where is a circular array.
 *
 * The `begin_index_element` is inclusive and the `end_index_element` is exclusive.
 * `recording` is not modified.
 */
using AudioPublisher = void (*)(const int16_t* const recording, 
  const long array_length, const long begin_index_element, 
  const long end_index_element);

using RnnoiseProcessor = float (*)(const float in_frames[NUMBER_FRAMES_RNNOISE], 
  float out_frames[NUMBER_FRAMES_RNNOISE]);

/**
 * @param {const int16_t*} input_frames An array with `NUMBER_FRAMES_RNNOISE` elements.
 */
using RnnoiseNewInputProcessor = void(*)(const int16_t* input_frames, 
  const RnnoiseProcessor rnnoise_process, const AudioPublisher audio_publisher,
  const bool publish_without_noise);

} // namespace detection_algorithms
} // namespace rnnoise_methods
#endif
