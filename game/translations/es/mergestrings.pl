#!/usr/bin/perl
%FOUND = ();
for my $line (<>) {
        if ($line=~/^#/s) {
                print $line;
        } elsif (exists($FOUND{$line})) {
                if ($line ne $lastline) {
                        print STDERR "Skipping duplicate line $line";
                }
        } else {
                $FOUND{$line} = 1;
                print $line;
                print $line;
        }
        $lastline = $line;
}
