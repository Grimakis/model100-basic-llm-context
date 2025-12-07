# The Sound Generator

## Sound Generator Commands

BEEP Causes the sound generator to "beep" for approximately 1/2
second.
BEEP


SOUND pitch, length "Plays" a given pitch for the given length.
length ranges from 0 to 255. Dividing length by 50 gives the
approximate length in seconds. pitch ranges from 0 to 16383, with
the smaller values corresponding to higher pitches.
SOUND 4500.50


**SOUND ON or OFF** Enables or disables "beep" when:
* You're loading from cassette
* The Model 100 is waiting on a carrier signal from the telephone modem lines.
SOUND ON
SOUND OFF


SOUND Pitch Values Corresponding to Standard Musical notes
<table id="21-1">
<tr><td id="21-2"></td><td id="21-3" colspan="5">Octave</td></tr>
<tr><td id="21-4">Note</td><td id="21-5">1</td><td id="21-6">2</td><td id="21-7">3</td><td id="21-8">4</td><td id="21-9">5</td></tr>
<tr><td id="21-a">G</td><td id="21-b">12538</td><td id="21-c">6269</td><td id="21-d">3134</td><td id="21-e">1567</td><td id="21-f">83</td></tr>
<tr><td id="21-g">G#</td><td id="21-h">11836</td><td id="21-i">5918</td><td id="21-j">2959</td><td id="21-k">1479</td><td id="21-l">739</td></tr>
<tr><td id="21-m">A</td><td id="21-n">11172</td><td id="21-o">5586</td><td id="21-p">2793</td><td id="21-q">1396</td><td id="21-r">698</td></tr>
<tr><td id="21-s">A#</td><td id="21-t">10544</td><td id="21-u">5272</td><td id="21-v">2636</td><td id="21-w">1318</td><td id="21-x">659</td></tr>
<tr><td id="21-y">B</td><td id="21-z">9952</td><td id="21-A">4976</td><td id="21-B">2488</td><td id="21-C">1244</td><td id="21-D">62</td></tr>
<tr><td id="21-E">C</td><td id="21-F">9394</td><td id="21-G">4697</td><td id="21-H">2348</td><td id="21-I">1174</td><td id="21-J">587</td></tr>
<tr><td id="21-K">C#</td><td id="21-L">8866</td><td id="21-M">4433</td><td id="21-N">2216</td><td id="21-O">1108</td><td id="21-P">554</td></tr>
<tr><td id="21-Q">D</td><td id="21-R">8368</td><td id="21-S">4184</td><td id="21-T">2092</td><td id="21-U">1046</td><td id="21-V">523</td></tr>
<tr><td id="21-W">D#</td><td id="21-X">7900</td><td id="21-Y">3950</td><td id="21-Z">1975</td><td id="21-10">987</td><td id="21-11">493</td></tr>
<tr><td id="21-12">E</td><td id="21-13">7456</td><td id="21-14">3728</td><td id="21-15">1864</td><td id="21-16">932</td><td id="21-17">466</td></tr>
<tr><td id="21-18">F</td><td id="21-19">7032</td><td id="21-1a">3516</td><td id="21-1b">1758</td><td id="21-1c">879</td><td id="21-1d">439</td></tr>
<tr><td id="21-1e">F#</td><td id="21-1f">6642</td><td id="21-1g">3321</td><td id="21-1h">1660</td><td id="21-1i">830</td><td id="21-1j">415</td></tr>
</table>


<table id="21-1k">
