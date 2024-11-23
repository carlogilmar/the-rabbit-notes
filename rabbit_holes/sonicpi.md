# Sonic Pi

Concepts to know:

Sonic Pi Essentials

- `BPM` stands for Beats Per Minute. It’s a unit of measurement for the tempo or speed of a song, indicating how many beats (or rhythmic pulses) occur in one minute.
- `live_loop` is a key feature of Sonic Pi that allows you to repeat a block of code indefinitely
- `use_synth :fm`: Use the FM (Frequency Modulation) synthesizer for generating sounds. Synths: `:tb303`, `:prophet`
- `play_pattern_timed`: This is a function that plays a sequence of notes (a pattern) at a specified time interval.
- `amp: 1.5`: This controls the volume (amplitude) of the sound.
- `release: 0.5`: This controls how long the note's sound will continue after you press it.
- `sync` command: It tells this loop to wait for the `:bassline` loop to finish its current iteration before it starts playing.

`Billie Jean`
```ruby
# Set BPM
use_bpm 118

# Iconic Bassline
live_loop :bassline do
  use_synth :fm
  play_pattern_timed [:g2, :g2, :g2, :g2, :a2, :a2, :a2, :g2],
    [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
    amp: 1.5, # volume
    release: 0.5 # how long will continue
end

# Chords for Harmony
live_loop :chords do
  sync :bassline
  use_synth :piano
  play_chord [:g3, :b3, :d4], release: 2
  sleep 2
  play_chord [:a3, :c4, :e4], release: 2
  sleep 2
end

# Beat
live_loop :drums do
  sample :bd_808, amp: 1.5
  sleep 0.5
  sample :sn_dub, amp: 1.2
  sleep 0.5
  sample :bd_808, amp: 1.5
  sleep 0.5
  sample :drum_cymbal_closed, amp: 0.8
  sleep 0.5
end

# Melody Hint (optional)
live_loop :melody do
  sync :bassline
  use_synth :pluck
  
  # Simplified vocal hint
  play_pattern_timed [:b4, :c5, :d5, :e5], [0.25, 0.25, 0.5, 1], amp: 1.2
  sleep 1.5
end
```


## Documentation Examples

```ruby
live_loop :flibble do
  sample :bd_haus, rate: 1
  sleep 0.5
end
```

```ruby
live_loop :flibble do
  sample :ambi_choir, rate: 0.5
  sample :bd_haus, rate: 2
  sleep 1
end
```

```ruby
live_loop :guit do
  with_fx :echo, mix: 0.3, phase: 0.25 do
    sample :guit_em9, rate: 0.5
  end
  
  sample :guit_em9, rate: -0.5
  sleep 8
end

live_loop :boom do
  with_fx :reverb, room: 1 do
    sample :bd_boom, amp: 10, rate: 1
  end
  sleep 8
end
```

```ruby
# This is a Beat
play 72
sleep 0.5
play 75
sleep 0.5
play 79
```

```ruby
# Play random notes
100.times do
  play rrand_i(60, 90)
  sleep 0.5
end
```

```ruby
# Play a chord
loop do
  play chord(60, :M7).tick
  sleep 0.5
end
```

```ruby
## Example 5 - play a chord with an arpeggio
loop do
  play chord(60, :M7), release: 3
  16.times do
    play chord(60, :M7).choose
    sleep 0.25
  end
end
```

```ruby
## Example 6 - play a shifting chord with an arpeggio
start_notes = ring(60, 62, 63, 62)
loop do
  my_chord = chord(start_notes.tick, :M7)
  play my_chord, release: 2
  16.times do
    play my_chord.choose
    sleep 0.125
  end
end
```

```ruby
## Example 7 - play a drum
sample :drum_bass_hard
```

```ruby
# Cool drumps
live_loop :drums do
  sample :loop_amen, beat_stretch: 2,amp:0.5
  sleep 2
  sample :elec_plip
end
```

```ruby
# Song
# theme interpretation of a "conventional" rock song
# SonicPi version: https://soundcloud.com/open_horse_music/blackminded-rsjp-vague-sonic-pi-interpretation-v2

tick   = 1.0
half   = 0.5*tick
quart  = 0.25*tick
length = 32*tick

in_thread(name: :letsgetloud) do
  sync :frame
  sleep length
  loop do
    drums_please_get_loud
  end
end

define :permanent_drumset do
  length.to_i.times.each_with_index do |_, i|
    sample :drum_cymbal_closed
    sleep tick
  end
end

define :drums_please_get_loud do
  length.to_i.times.each_with_index do |_, i|
    with_fx :level, amp: 2.0 do
      sample :drum_bass_hard
      sleep half
      sample :drum_snare_hard
      sample :drum_cymbal_hard if i % 8 == 3
      sleep half
    end
  end
end

define :monolithic_pattern do
  4.times do
    [:a3, :cs4, :a4, :cs4].each do |note|
      play note
      sleep quart
    end
  end

  2.times do
    [:ab3, :cs4, :ab4, :cs4].each do |note|
      play note
      sleep quart
    end
  end

  1.times do
    [:ab3, :cs4, 66, :cs4].each do |note|
      play note
      sleep quart
    end
  end

  1.times do
    [56, :cs4, 65, :cs4].each do |note|
      play note
      sleep quart
    end
  end


  4.times do
    [57, :d3, 66, :d3].each do |note|
      play note
      sleep quart
    end
  end

  4.times do
    [54, :b2, 66, :b2].each do |note|
      play note
      sleep quart
    end
  end
end

in_thread(name: :the_red_line) do
  sync :frame
  loop do
    with_synth :sine do
      monolithic_pattern
    end
  end
end

in_thread(name: :groll) do
  sync :frame
  sleep 16*tick
  loop do
    sleep 12*tick
    with_fx :level, amp: 2.0 do
      with_synth(:fm) do
        with_fx(:distortion) do
          4.times do
            play 54.0
            sleep quart

            play :b2
            sleep quart

            #play 66.0
            sleep quart

            play :b2
            sleep quart
          end
        end
      end
    end
  end
end

in_thread(name: :screaming_git) do
  sync :frame
  sleep 48*tick
  loop do
    with_fx :level, amp: 0.4 do
      with_synth(:pulse) do
        with_fx(:distortion) do
          monolithic_pattern
        end
      end
    end
  end
end

in_thread(name: :supportive) do
  sync :frame
  sleep 16*tick
  loop do
    with_synth(:fm) do
      monolithic_pattern
    end
  end
end

in_thread(name: :supportive_dist) do
  sync :frame
  sleep 64*tick
  loop do
    with_synth(:fm) do
      with_fx(:distortion) do
        monolithic_pattern
      end
    end
  end
end

in_thread(name: :frame) do
  cue :frame
  loop do
    permanent_drumset
  end
end
```

```ruby

#just play around with commenting things out/ removing them and adding them again 
#my version of this can be found here: https://soundcloud.com/langziehohr/first

live_loop :flibble do

play 60, amp: 0.1
sleep 0.25
play 65, amp: 0.2
sleep 0.5
play 60, amp: 0.1
sleep 0.25
play 63, amp: 0.2
sleep 0.5
play 60, amp: 0.1
sleep 0.25
play 62, amp: 0.2
sleep 0.5
play 60, amp: 0.1
sleep 0.25
play 63, amp: 0.2
sleep 0.5



end

live_loop :mau do 
# sample :bd_haus, rate: 1, amp: 0.4
  sleep 0.75
end

live_loop :mia do
# sample :bd_haus, rate: 0.8, amp: 0.4
  sleep 1
end 


live_loop :miez do
#sample :drum_cymbal_closed, amp: 0.1
sleep 0.25

end

live_loop :mauz do
# sample :drum_cymbal_pedal, amp: 0.2
  sleep 1.5

end 

live_loop :mauz2 do
#  sample :bd_fat
sleep 3
end
```
