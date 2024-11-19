# Sonic Pi

Concepts to know:

- Beat `play 70`

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
