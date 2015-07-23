#!/usr/bin/perl
$line = 1;
$lineno = 0;
%FIRST_LINE_SEEN = ();
while (defined($line)) {
        $line = <>;
        $lineno += 1;
        if ($line=~/^#/s) {
                next;
        }
        if ($lineno==1) {
                print "Debug: line 1: $line";
        }
        $SEEN{$line}++;
        if ($SEEN{$line}>=2) {
                print "Duplication: $lineno: $line";
                print "(Originally on $FIRST_LINE_SEEN{$line})";
                $line = <>;
                print "Translated to: $line";
                $lineno++;
        } else {
                $FIRST_LINE_SEEN{$line} = $lineno;
                $line = <>;
                $lineno++;
        }
}
